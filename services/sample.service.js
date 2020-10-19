const database = require("../database");

exports.createSample = function (id, name) {
  database().then((db) => {
    db.query("INSERT INTO SAMPLE VALUE (?, ?)", [id, name]);
  });
};
