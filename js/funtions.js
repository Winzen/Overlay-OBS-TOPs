
let where = 60
let where2 = 0
let positon = 100


function move_() {
    let c = document.getElementsByClassName("lado_position_winner");
    
        for (let i = 0; i < c.length; i++) {
            c[i].style.paddingTop  = `${where}%`;   
            }
    where -= 1;
    
    return where;
    
};

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function anima() {
    while (true){
        await sleep(20);
        where = move_();
        if (where < 0){
            return where;
        };
    };
    
};

function linha_show(){
    let linhas = document.getElementsByClassName("linha_animado");
    for (let x = 0; x < linhas.length; x++){
        linhas[x].style.opacity = "1.0"
    };
    return linhas
}

function move_2() {
    let c = document.getElementsByClassName("text_animado");
    
        for (let i = 0; i < c.length; i++) {
            c[i].style.height = `${where2}%`;   
            }
    where2 += 5;
    
    return where2;
    
};

async function anima2() {
    await sleep(1000)
    while (true){
        await sleep(5);
        where2 = move_2();
        if (where2 > 99){
            linha_show()
            
            return where2;
        };
    };
    
};

function check(box) {
    let txt = document.querySelector('.name_to_extra_long');
    let body = document.querySelector(box);
    const rect = txt.getBoundingClientRect();
    const rect2 = body.getBoundingClientRect();
    let sair = (rect.width/rect2.width)*100+10
    if(positon < -sair){
        return true
    }
    console.log((rect.width/rect2.width)*100, positon, box)
  
}

function mover_name(box){
    let mensage = document.getElementsByClassName("name_to_extra_long");
    for(let i = 0; i < mensage.length; i++){
        mensage[i].style.left = `${positon}%`;
    };
    positon -= 0.25;

    if(check(box)){
        positon = 100;
    }
    return positon;
}

function movimetation(box){

    return setInterval(() => {positon = mover_name(box); return positon;}, 1)
}

function FitText(box, target_) {
    let txt = document.getElementsByClassName(target_);
    let body = document.getElementsByClassName(box);
    // console.log(body)
    // let rect = txt.getBoundingClientRect();
    // let rect2 = body.getBoundingClientRect();
    // let sair = (rect.width/rect2.width)*100+10
    
    for(let i = 0; i < body.length; i++){
      let scalex_ = 1
      let target__ = txt[i].getBoundingClientRect();
      let element_ = body[i].getBoundingClientRect();
    //   console.log(body[i].textContent)
      while(scalex_ > 0){

          body[i].style.transform = `ScaleX(${scalex_})`
          scalex_ -= 0.01
          target__ = txt[i].getBoundingClientRect();
          element_ = body[i].getBoundingClientRect();
        //   console.log(target__.width, element_.width , scalex_)
          if(target__.width > element_.width){
              break
          }
        
          

      }
  }
    
  
};

function limite_name(tag){
    let txt = document.getElementsByClassName(tag);
    for (let h = 0; h < txt.length; h++){
        let nick = txt[h].textContent.trim()
        if(nick.length > 30){
            txt[h].textContent = `${nick.slice(0, 27)}...`;
        }

    }

};

limite_name("fitname");
FitText("fitname", "div_name_jogador");
