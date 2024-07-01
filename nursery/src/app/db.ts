// lib/db.js
import { Pool } from 'pg';

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'postgres',
  password: '1234',
  port: 5432, // default PostgreSQL port
});

export const query = (text: string, params?: any[]) => pool.query(text, params);
