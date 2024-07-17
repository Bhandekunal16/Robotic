const Response = require("robotic.js/src/class/response");

class Binary {
  convertToBinary(input) {
    try {
      if (input == undefined)
        return new Response().badRequest("input not be undefined");

      if (typeof input !== "string")
        throw new Response().badRequest("Input must be a string");

      let binary = "";
      for (let i = 0; i < input.length; i++) {
        let charCode = input.charCodeAt(i).toString(2);
        binary += this.padLeft(charCode, 8);
      }
      return binary;
    } catch (error) {
      return new Response().error(error);
    }
  }

  convertToString = (input) => {
    try {
      let string = "";

      if (input == undefined)
        return new Response().badRequest("input not be undefined");

      if (typeof input !== "string")
        throw new Response().badRequest("Input must be a string");

      for (let i = 0; i < input.length; i += 8) {
        let binaryCode = input.substr(i, 8);
        let charCode = parseInt(binaryCode, 2);
        string += String.fromCharCode(charCode);
      }

      return string;
    } catch (error) {
      return error;
    }
  };

  padLeft(str, length) {
    return "0".repeat(length - str.length) + str;
  }
}

module.exports = Binary;