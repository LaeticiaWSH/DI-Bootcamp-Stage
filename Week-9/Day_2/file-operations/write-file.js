const fs = require('fs');

fs.writeFile('output.txt','simple text content', function(err){
    if(err){
        console.log(err)
    }
    else{
        console.log('Write operation complete.')
    }
});