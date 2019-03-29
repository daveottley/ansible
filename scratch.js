let old_onclick = plus.onclick;
plus.onclick = async function (event) {
    for(let i = 0; i < 20; i++) {
        old_onclick(event);
        console.log(i);
        await sleep(1);
    }
}