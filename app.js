var gplay = require('google-play-scraper');

async function search_apps(t) {
    let abc = await gplay.search({term: t, num: 100, country: 'in'});
    return abc;
}

async function main() {
    let terms = ["loan", "cash", "app", "rupee", "credit", "money", "paisa", "coin", "wallet", "easy", "pocket"];
    appslist = []
    for (const term of terms){
        let temp = await search_apps(term);
        appslist.push(...temp);
        // console.log(appslist.length);
    }
    console.log(appslist);
}

main();