// import moment from "moment/moment";
async function main() {
    try {
        console.log('Hello, world!');
        return `[${Date.UTC()}] Its working!!!!!!!!!`;
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