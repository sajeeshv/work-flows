const moment = require('moment');
async function main() {
    try {

        console.log('Hello, world!');
        return `[${moment.utc().format("DD-MM-YYYY hh:mm:s A")}] Its working!!!!!!!!!`;
    } catch (error) {
        console.error('Error in main function', error);
        return error;
    }
}
(async () => {
    res = await main();
    console.log(res);
    return res;
}
)()