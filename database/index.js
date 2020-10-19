const mariadb = require("mariadb");
const config = require("./config");

async function database() {
  const pool = await mariadb.createPool({
    ...config,
    connectionLimit: 5,
  });

  const connection = await pool.getConnection();
  return connection;
}

module.exports = database;
