const SampleServices = require("./sample.service");

describe("Sample Service Tests[Shiwon]", () => {
  test("Read", (done) => {
    SampleServices.getAll()
      .then(() => {
        done();
      })
      .catch(done);
  });

  test("Write", (done) => {
    const id = Date.now();
    SampleServices.create(id, "Test Item")
      .then(() => {
        done();
      })
      .catch(done);
  });

  test("Prevent Duplicate", (done) => {
    const id = Date.now();
    SampleServices.create(id, "Prevent Duplicate")
      .then(() => {
        SampleServices.create(id, "Prevent Duplicate - 2")
          .then(() => {
            done(new Error("Duplicate Key Exists"));
          })
          .catch(() => {
            done();
          });
      })
      .catch(done);
  });

  test("Get One By Id", (done) => {
    SampleServices.getOneById("123")
      .then(() => {
        done();
      })
      .catch(done);
  });
});
