const database = require("../database");

// READ QUERY
database().then((db) => {
  db.query("SELECT * FROM SAMPLE;").then((rows) => {
    for (let row of rows) {
      console.log(row);
    }
    db.end();
  });
});

// for more, refer to https://mariadb.com/kb/en/getting-started-with-the-nodejs-connector/
