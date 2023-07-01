let urls = [
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/1_tfp0yo.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/2_z4n3rs.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/3_ymcuuc.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/4_dsmczb.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173317/5_lmixou.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/6_dexnkd.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/7_rm8krm.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/8_ewfmua.png',
    'https://res.cloudinary.com/dgzv7gan8/image/upload/v1688173318/1_tfp0yo.png',
];

let immage = document.querySelector('.rotating-immages');

for (let i = 0; i < urls.length; i++) {
    setTimeout(() => {
        immage.src = urls[i];
    }, 500 * i);
}