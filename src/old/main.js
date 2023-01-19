const request = require('request');
const cheerio = require('cheerio');
const { Builder, By, until } = require('selenium-webdriver');

async function getDownloadLink(itemId) {
  try {
    // Send a GET request to the collection URL and retrieve the HTML source code
    let url = `https://smods.ru/?s=${itemId}&app=255710`;
    console.log(`approaching url, `, url);

    let htmlContent = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        resolve(body);
      });
    });

    // Use cheerio to parse the HTML content
    let $ = cheerio.load(htmlContent);

    // Find the div with class "post-inner"
    let postInnerDiv = $('div.post-inner');

    // Find the anchor with class "skymods-excerpt-btn" that is a grandchild of the div
    let skymodsAnchor = postInnerDiv.findAll('a.skymods-excerpt-btn')[0];

    // Extract the href from the anchor
    let href = skymodsAnchor.attr('href');

    console.log('Got one link, ', href);
    return href;
  } catch (e) {
    console.log(`Except "${e}" occurred in ${itemId} with url, ${url}`);
    return '';
  }
}

async function getDownloadLinks(itemIds) {
  let links = await Promise.all(
    itemIds.map((itemId) => getDownloadLink(itemId))
  );
  return links;
}

async function openSteamLinks(fileLocation) {
  // open links from links.txt
  let urls = await new Promise((resolve, reject) => {
    fs.readFile(fileLocation, 'utf8', (err, data) => {
      if (err) reject(err);
      resolve(data.split('\n'));
    });
  });

  // Create an empty list to store the item ids
  let itemIds = [];

  // Iterate through the links
  for (let url of urls) {
    // Send a GET request to the collection URL and retrieve the HTML source code
    let htmlContent = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        resolve(body);
      });
    });

    // Use cheerio to parse the HTML content
    let $ = cheerio.load(htmlContent);
    let collection = $('div.collectionChildren');

    // Extract the item ids from the HTML source code
    collection.findAll('div.workshopItem').forEach((div) => {
      div.findAll('a').forEach((a) => {
        let queryParams = new URLSearchParams(new URL(a.href).search);
        let id = queryParams.get('id');
        itemIds.push(id);
      });
    });
  }

  console.log(itemIds);
  let links = await getDownloadLinks(itemIds);
  console.log(links);

  return links;
}
