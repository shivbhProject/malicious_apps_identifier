var gplay = require('google-play-scraper');

async function search_apps(t) {
    let abc = await gplay.search({ term: t, num: 200, country: 'in', fullDetail: true });
    return abc;
}

async function get_permissions(id) {
    let abc = await gplay.permissions({ appId: id });
    return abc;
}

async function main() {

    let filter_inr = true;
    let filter_email = true;

    let terms = ["loan", "cash", "app", "rupee", "credit", "money", "paisa", "coin", "wallet", "easy", "pocket"];
    appslist = []
    for (const term of terms) {
        let temp = await search_apps(term);
        appslist.push(...temp);
    }
    // console.log(appslist.length);
    // console.log(appslist);

    let allapps = [...new Set(appslist)];
    let filtered_list = [];
    for (const app of allapps) {
        if (app.currency == "INR" && (app.developerEmail == "" || (app.developerEmail.endsWith("@gmail.com")) || (app.developerEmail.endsWith("@hotmail.com")) || (app.developerEmail.endsWith("@yahoo.com")))) {

            let perms = await get_permissions(app.appId);
            for (const perm of perms) {
                if (perm.type == "Camera" || perm.type == "Microphone") {
                    filtered_list.push(app);
                    console.log(app.title, ", ", app.appId, ", ", app.currency, ", ", app.developerEmail, ", ", perm.type);
                    break;
                }
            }
        }
    }

    // console.log(filtered_list);
}

main();