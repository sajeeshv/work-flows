const moment = require('moment');
async function main() {
    try {
        throw new Error('This is an error');
        console.log('Hello, world!');
        return `[${moment.utc().format("DD-MM-YYYY hh:mm:ss A")}] Its working!!!!!!!!!`;
    } catch (error) {
        console.error('Error in main function', error);
        return error;
    }
}
(async () => {
    try {
        console.log('Starting the js script');
        res = await main();
        console.log(res);
        return res;
    } catch (error) {
        console.error('Error in async function', error);
        return error;
    }
}
)()