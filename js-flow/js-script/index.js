const moment = require('moment');
async function main() {
    console.log('Hello, world!');
    return `[${moment.utc().format("DD-MM-YYYY hh:mm:s A")}] Its working!!!!!!!!!`;
}
(async () => {
    res = await main();
    console.log(res);
    return res;
}
)()