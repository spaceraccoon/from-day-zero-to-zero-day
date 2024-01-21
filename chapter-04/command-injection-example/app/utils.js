const { execSync } = require("child_process");

exports.ping = (ip) => {
  try {
    return execSync(`ping -c 5 ${ip}`);
  } catch (error) {
    return error.message;
  }
};