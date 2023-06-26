let urls = [
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1687819244/30_ma1y74.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1687819244/27_gfuraf.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1687819243/28_epjhbo.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1687819243/22_ef27pw.png',
];

let immage = document.querySelector('.rotating-immages');

for (let i = 0; i < urls.length; i++) {
    setTimeout(() => {
        immage.src = urls[i];
    }, 500 * i);
}