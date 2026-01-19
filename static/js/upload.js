async function upload() {
    const file = document.getElementById("audio").files[0];
    if (!file) return alert("Dosya seç");

    const fd = new FormData();
    fd.append("audio", file);

    const res = await fetch("/upload", {
        method: "POST",
        body: fd
    });

    const data = await res.json();

    document.getElementById("result").innerText =
        "🎧 Metin:\n" + data.transcript +
        "\n\n🤖 Cevap:\n" + data.response;
}
