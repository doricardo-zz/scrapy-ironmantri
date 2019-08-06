eel.expose(loadRaces);
async function loadRaces() {
    let value = await eel.loadRaces()();
    alert(value);
}