import type { NextApiRequest, NextApiResponse } from 'next';
import { query } from '../../app/db';
import { promises as fs } from 'fs';
import path from 'path';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    const { name } = req.query as { name: string }; // Get plant name from query parameter
  
    if (!name) {
      return res.status(400).json({ message: 'Missing required parameter: name' });
    }
  
    try {
      const plantData = await getPlantData(name); // Call your function to fetch plant data
  
      const filePath = path.join(process.cwd(), 'public', `${name}.json`);
      await fs.writeFile(filePath, JSON.stringify(plantData, null, 2));
  
      res.setHeader('Content-Disposition', `attachment; filename=${name}.json`);
      res.setHeader('Content-Type', 'application/json');
  
      const fileData = await fs.readFile(filePath, 'utf-8'); // Read as a string for JSON data
      res.status(200).json(JSON.parse(fileData)); // Parse the data before sending
    } 
    catch (error) {
      console.error('Error fetching or processing data:', error);
      res.status(500).json({ message: 'Internal server error' });
  }
  }

  
  async function getPlantData(name: string): Promise<any> {
    try {
        const result = await query(`
          SELECT json_agg(row_to_json(t))
          FROM (
            SELECT name, water, sunlight, lifespan, fruit_nut, fertilizer, pest, comp_plants
            FROM plant
            WHERE plant.name = $1
          ) t
        `, [name]);
    
        if (result.rows.length === 0) {
          return null; // Plant not found
        }
    
        return result.rows[0].json_agg; // Type assertion for clarity
      } catch (error) {
        console.error('Error fetching plant data:', error);
        throw error; // Re-throw the error for proper handling in the API route
      }
  }