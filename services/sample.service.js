const database = require("../database");

// for more, refer to https://mariadb.com/kb/en/getting-started-with-the-nodejs-connector/

const create = async function (id, name) {
  // const db = await database();
  // await db.query("INSERT INTO SAMPLE VALUE (?, ?)", [id, name]);
  // db.end();
};

const getAll = async function () {
  // const db = await database();
  // const samples = await db.query("SELECT * FROM SAMPLE");
  // db.end();
  // return samples;
};

const getOneById = async function (id) {
  // const db = await database();
  // const samples = await db.query("SELECT * FROM SAMPLE WHERE Id=?", [id]);
  // db.end();
  // return samples;
};

const SampleServices = {
  create,
  getAll,
  getOneById,
};

module.exports = SampleServices;
