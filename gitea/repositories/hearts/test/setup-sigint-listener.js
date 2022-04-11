// make sure that all garbage gets collected on SIGINT
process.on('SIGINT', process.exit);
