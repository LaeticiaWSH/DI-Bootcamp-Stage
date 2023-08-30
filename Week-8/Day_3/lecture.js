// An asynchronous function that resolves after a delay
function resolveAfterDelay(delay) {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('Resolved after ' + delay + ' milliseconds');
        }, delay);
    });
}

// An async function that calls the resolveAfterDelay function
async function doAsyncTask() {
    try {
        const result = await resolveAfterDelay(2000); // Wait for the promise to resolve
        console.log(result);
        console.log("The result has come.")
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the async function
doAsyncTask();