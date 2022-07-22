var gplay = require('google-play-scraper');

async function search_apps(t) {
    let abc = await gplay.search({term: t, num: 100, country: 'in', fullDetail: true});
    return abc;
}

async function get_permissions(app_id) {
    let abc = await gplay.app({appId: app_id});
    // return abc.permissions;
    console.log(abc.permissions);
}

async function main() {

    let filter_inr = true;
    let filter_email = true;

    let terms = ["loan", "cash", "app", "rupee", "credit", "money", "paisa", "coin", "wallet", "easy", "pocket"];
    appslist = []
    for (const term of terms){
        let temp = await search_apps(term);
        appslist.push(...temp);
    }
    // console.log(appslist.length);
    // console.log(appslist);

    let filtered_list = [];
    for (const app of appslist){
        // console.log(app.developerEmail, app.currency);
        if(app.currency == "INR" && (app.developerEmail == "" || (app.developerEmail.endsWith("@gmail.com")) || (app.developerEmail.endsWith("@hotmail.com")) || (app.developerEmail.endsWith("@yahoo.com")))){
            filtered_list.push(app);

            await get_permissions(app.appId);
            // console.log(perm);
        }
        // if(filter_email && (app.developerEmail != "" || (app.developerEmail.endsWith("@gmail.com")) || (app.developerEmail.endsWith("@hotmail.com")) || (app.developerEmail.endsWith("@yahoo.com")))){
        //     filtered_list.push(app);
        // }
    }

    // console.log(filtered_list);
}

main();