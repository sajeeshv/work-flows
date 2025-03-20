const moment = require('moment');
const {
    ApiClient, RecordsApi
} = require('@thingspine/api-client',);

const apiClient = new ApiClient('https://api.nael.thingspine.com',); // instantiate the ApiClient
const ApiClientAuth = apiClient.authentications.basicAuth;
ApiClientAuth.username = "2400f6c5-3746-422a-99e0-366e9d2e9e33"; // set basic auth credentials in api client
ApiClientAuth.password = "~JidZjjBTrvTiqqbeWk1FTd2rF";
const recordsApi = new RecordsApi(apiClient,); // instantiate the records api

async function main() {
    try {
        console.log('Hello, world!');
        const data = await getData()
        return data;
    } catch (error) {
        console.error('Error in main function', error);
        return error;
    }
}
async function getData() {
    try {
        const promise = new Promise((resolve, reject) => {
            recordsApi.listRecords("67af10ca15045c0335ca135c", "Meter", {
                "select": ["id", "customerId", "serviceId", "meterNumber", "meterEntityId", "status"]
            }, (error, data, response) => {
                if (error) {
                    reject(error);
                } else {
                    resolve(response.body);
                }
            });
        });
        const meters = await promise;
        return meters
    } catch (error) {
        console.error('Error in getData function', error);
        return error;
    }
}
(async () => {
    try {
        res = await main();
        console.log(res);
        // return res;
    } catch (error) {
        console.error('Error in async function', error);
        // return error;
    }
}
)()