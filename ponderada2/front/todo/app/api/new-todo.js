export default function handler(req, res) {
    if (req.method === 'GET') {
        res.status(200).json(notes)
    } else if (req.method === 'POST') {
        const note = req.body.note
        const newNote = {
            id: Date.now(),
            description: note,
            owner_id: "1"
        }
        notes.push(newNote)
        res.status(201).json(newNote)
    }
}