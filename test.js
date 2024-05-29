const myPromise = new Promise((resolve, reject) => {
let x = 1;
    try {
        if (x === 1) { //caso de fallo en donde no se cumple la condicio nde la promesa
            throw new Error("hubo un error")
        }
        resolve(
            console.log("test")
        )    
    } catch (error) {
        reject(console.log("hubo un error ", error))
    }
  });
  
  const test1 = () => {
    console.log("fallo")
  }

  const test2 = () => {
    console.log("funcion")
  }

myPromise
    .then(test2, test1);
  