import express from 'express'

const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.json({
        "message": "Hello from a container",
        "service": "hello-node",
        "pod": process.env.POD_NAME || "unknown POD",
        "time": new Date().toISOString()

    })
})

app.get("/readyz", (req, res) => res.status(200).json("ready"))
app.get("/healthz", (req, res) => res.status(200).json("ok"))

app.listen(PORT, ()=>{
    console.log(`Example app listening on ${PORT}!`);
})
