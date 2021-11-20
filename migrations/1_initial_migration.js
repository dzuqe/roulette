//const Migrations = artifacts.require("Migrations");
const Roulette = artifacts.require("Roulette");

module.exports = function (deployer) {
  deployer.deploy(Roulette);
};
