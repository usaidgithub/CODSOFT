document.addEventListener('DOMContentLoaded',async()=>{
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');
    let modal=document.getElementsByClassName('form')[0]
    let close=document.getElementsByClassName('close-icon')[0]
    let input=document.getElementById('id')
    addTaskBtn.addEventListener('click',(e)=>{
        e.preventDefault()
        const taskText = taskInput.value.trim();
        
        const data = { records: taskText };
        console.log(`The data is ${data.records}`)
        // Send an HTTP POST request to the Flask server using fetch
        fetch('http://127.0.0.1:5000/add_record', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
            
        })
        .then(data => {
            console.log('Successfully retreived data',data);
            // Optionally update the UI if needed
            showToast("Record Added Successfully Please Refresh the page")
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors, show user feedback, etc.
        });
   
    })
    const getResponse=await fetch('http://127.0.0.1:5000/get_records')
        if (!getResponse.ok) {
            throw new Error('Failed to fetch tasks');
        }
        const recordhtml=document.querySelector('.task_container')
        const tasks = await getResponse.json();
        console.log(tasks)
        tasks.forEach(record=>{
            const taskhtml=`
            <div class="expenses_records" data-id="${record.id}">
            <span>Record:${record.records}</span>
            <span>Date:${(record.date).toLocaleString()}</span>
            <button class="edit_expenses">Edit</button>
            <button class="delete_expenses">Delete</button>
            </div>`
            recordhtml.innerHTML+=taskhtml
        })
        document.querySelectorAll('.delete_expenses').forEach(button=>{
            button.addEventListener('click',handleexpensesdeletion)
        })

        document.querySelectorAll('.edit_expenses').forEach(button=>{
            button.addEventListener('click',(event)=>{
                const recordId=event.target.closest('.expenses_records').dataset.id
                console.log(`Record id from expenses table is ${recordId}`)
                input.value=recordId
                console.log(`The input value is ${input.value}`)
               modal.style.display="block"
               event.preventDefault()
            })
        })
       close.addEventListener('click',(e)=>{
        modal.style.display="none"
       })
    })
    async function handleexpensesdeletion(event){
        const recordId=event.target.closest('.expenses_records').dataset.id
        console.log(`Record id from expenses table is ${recordId}`)
        await fetch(`http://localhost:5000/delete_record/${recordId}`,{
            method:'DELETE'
        }).then(response=>{
            if(response.ok){
                event.target.closest('.expenses_records').remove()
            }else{
                console.log("Error in deleting expenses data")
            }
        }).catch(error=>{
            console.log("Error on fetching",error)
        })
    
    }
    function showToast(message) {
        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.textContent = message;
    
        document.body.appendChild(toast);
    
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 3000); // Adjust the timeout as needed
    }
    
