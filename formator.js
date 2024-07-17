const shape = 
    require("robotic.file.converter/converter.v2");

class  App {  application(path) {    new shape().readLines(path);
}}const app = new App();

        if  (
    require.main === 
module ) {  const path = process.argv[2];
  app.application(path);
}
module .exports = App;
