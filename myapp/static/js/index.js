$(document).ready(function (){
    $('.owl-carousel').owlCarousel({
        items:1,
        loop:true, 
        autoplay:true,
        autoplayTimeout:2000,
        autoplayHoverPause:true,
        nav : true,
        dots : false,
    });
    $('.play').on('click',function(){
        owl.trigger('play.owl.autoplay',[1000])
    })
    $('.stop').on('click',function(){
        owl.trigger('stop.owl.autoplay')
    })


})
/*

// function for bottomwear display..

var image = 0; 

showImage(image)





function controller (x){

    image = image + x;
    showImage(image)
}


function showImage (img){

let sliders = document.getElementsByClassName('bottomwear-item');
let slider_len = sliders.length


if (img == slider_len){

    image = 0;
    img = 0;
}

if(img < 0 ){

    image = slider_len;
    img = slider_len;
}

 
sliders[img].style.display = 'block';

}





show()

function show(){

    items = document.getElementsByClassName('bottomwear-item');
    len = items.length;
    
    for(let i = 0 ; i < (len-5); i++){

        items[i].style.display = 'block'
    }
}






var image = 0; 

showImage(image)


function controller (x){

    image = image + x;
    showImage(image)
}


function showImage (img){

let sliders = document.getElementsByClassName('bottomwear-item');
let slider_len = sliders.length;



if (img == slider_len){

    image = 0;
    img = 0;
}

if(img < 0 ){

    image = slider_len;
    img = slider_len;
}

for(let y of sliders){
    y.style.display = 'none'

    
}


 
sliders[img].style.display = 'block';

}
*/

$('#slider1').owlCarousel({
    loop:true,
    margin : 10,
    nav : true,
    dots:false,
    navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:5,
            nav:true,
            loop:true
        }
    }

    
})


$('#slider2').owlCarousel({
    loop:true,
    margin : 10,
    nav : true,
    dots:false,
    autoplay:true,
    autoplayTimeout:2000,
    navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:5,
            nav:true,
            loop:true
        }
    }

    
})

$('#slider3').owlCarousel({
    loop:true,
    margin : 10,
    nav : true,
    dots:false,
    navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:5,
            nav:true,
            loop:false
        }
    }

    
})

$('#slider4 , #slider5').owlCarousel({
    loop:true,
    margin : 10,
    nav : true,
    dots:false,
    navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:5,
            nav:true,
            loop:false
        }
    }

    
})


$('#slide').owlCarousel({
    loop:true,
    margin : 10,
    nav : true,
    dots:false,
    navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],

    responsiveClass:true,
    
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:5,
            nav:true,
            loop:false
        }
    }

    
})



/* function for profile dropdone content
function myfunc () {

    document.querySelector('#drpdncont').classList.toggle('show')

};

 function if the user click outside the button to hide the dropdown

window.onclick = function (event){
    if (!event.target.matches('#btnn')){

        let dropdowns = document.querySelector('#drpdncont');
    
        
            if (dropdowns.classList.contains('show')){

                dropdowns.classList.remove('show');

            }
        }

    }
*/
//product cart increasing function
$('.plus-cart').click(function (){
    let id = $(this).attr('pid').toString();
    let ele = this.parentNode.children[2]


    $.ajax({
        type : 'GET' ,
        url : '/pluscart',
        data : {
            prod_id : id
        },

        success : function(data){
            
            ele.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            
        }
        
})



})



$('.minus-cart').click(function(){
    let id = $(this).attr('pid').toString();
    let ele = this.parentNode.children[2]

    $.ajax({
        type : 'GET',
        url  : '/minuscart/',
        data : {
            prod_id : id
        },

        success : function(data){
        
            document.getElementById('quantity').innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            

        }


    })


})

$('#remove-cart').click(function (){
    let id  = $(this).attr('pid').toString();
    let ele = this

    $.ajax({
        type : 'GET',
        url : '/removecart/',
        data : {
            prod_id : id
        },

        success : function(data){
            
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
            ele.parentNode.parentNode.parentNode.parentNode.remove()
            
        }



    })


})

function myFun(){
    var x = document.getElementById('navba');
    if (x.className === "navbar"){
        x.className += "responsive"
    }
    else{
        x.className = "navbar";
    }
} 





