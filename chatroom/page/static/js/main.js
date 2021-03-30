
const UPDATE_TIME =700
let data = []


const fetchMessages = () => {
	fetch("http://0.0.0.0:8000/messages",
	{
	    headers: {
	      'Accept': 'application/json',
	      'Content-Type': 'application/json'
	    },
	    method: "GET"
	})
		.then(res => res.json())
		.then(res => {
			data = res.reverse()
	})
}

fetchMessages()

const messages = document.querySelector('.messages')

const render = (items) => {
	messagesHTML = ``
	
	items.map(item => {
		messagesHTML += `
				<div>
					<author>${item.author.username}</author>
					<h>${item.text}</h>
				<div>
			`
	})

	messages.innerHTML = messagesHTML

}

setInterval(()=>{
	fetchMessages()
	console.log(data)
	render(data)
}, UPDATE_TIME)




