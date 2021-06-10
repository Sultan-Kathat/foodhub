
     document.addEventListener('DOMContentLoaded', ()=>{
      document.querySelectorAll('#category').forEach(category=>{

        category.addEventListener('click', (c)=>{
          console.log(c.target);
          hide(c.target.innerHTML);
          //document.getElementById('test').innerHTML = c.target.innerHTML
          // document.querySelectorAll(".menu_item").forEach(item=>{
          //   if this.data.category = 

          // })
        })
      })
     })

     function hide(category_clicked){
      // console.log("inside hide")
      // console.log(category_clicked)
      document.querySelectorAll('.menu_item').forEach(menu=>{
        if (category_clicked === "Show All"){
          menu.classList.remove("d-none")
        }
        else{

          if (menu.dataset.category === category_clicked) {
            console.log(menu);
            menu.classList.remove("d-none")
          }
          else{
            menu.classList.add("d-none")
          }
        }

      })

     }

 