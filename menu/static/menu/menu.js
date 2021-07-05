

     document.addEventListener('DOMContentLoaded', ()=>{
      document.querySelector("#select_category").addEventListener('change',()=>{
        var e = document.getElementById("select_category").value;
        console.log(e)
        hide(e);
      })
          // var e = document.getElementById("select_category").value;
          
          // hide(e);
    
    })
     function hide(category_clicked){
      // console.log("inside hide")
      // console.log(category_clicked)
      // scroll back to top
      window.scrollTo(0, 176);
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

// add warning on clicking on back button
window.onbeforeunload = function () {
  // console.log("in loop")
  return 'Do you want to Leave Restaurant Menu ?'; 
}


// window.onscroll= ()=>{
//   var select_category = document.getElementById("div_select");
//   var select_title = document.getElementById("select_title");
//   select_title
//   if (window.scrollY > 175){
    
//     select_category.style.backgroundColor = "rgb(61, 60, 60)";
    
//     select_title.style.color = "white";
    
//   }

//   if (window.scrollY <=175){
//     select_category.style.backgroundColor = 'white';
//     select_title.style.color = "black";
//   }
// }



// below code can be used to get the distance of element from top and scroll to the element
// document.querySelectorAll('[data-category~="Sides"]');
// var el = document.querySelector('[data-category="Sides"]');
// var rect = el.getBoundingClientRect();
// console.log(rect.top, rect.right, rect.bottom, rect.left);
// window.scrollTo(0, 215);
