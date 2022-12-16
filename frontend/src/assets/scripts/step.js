var form_1 = document.querySelector(".form_1");
var form_2 = document.querySelector(".form_2");
var form_3 = document.querySelector(".form_3");
var form_4 = document.querySelector(".form_4");
var form_5 = document.querySelector(".form_5");

var form_1_btns = document.querySelector(".form_1_btns");
var form_2_btns = document.querySelector(".form_2_btns");
var form_3_btns = document.querySelector(".form_3_btns");
var form_4_btns = document.querySelector(".form_4_btns");
var form_5_btns = document.querySelector(".form_5_btns");

var form_1_next_btn = document.querySelector(".form_1_btns .btn_next");
var form_2_back_btn = document.querySelector(".form_2_btns .btn_back");
var form_2_next_btn = document.querySelector(".form_2_btns .btn_next");
var form_3_back_btn = document.querySelector(".form_3_btns .btn_back");
var form_3_next_btn = document.querySelector(".form_3_btns .btn_next");
var form_4_back_btn = document.querySelector(".form_4_btns .btn_back");
var form_4_next_btn = document.querySelector(".form_4_btns .btn_next");
var form_5_back_btn = document.querySelector(".form_5_btns .btn_back");

var form_2_progessbar = document.querySelector(".form_2_progessbar");
var form_3_progessbar = document.querySelector(".form_3_progessbar");
var form_4_progessbar = document.querySelector(".form_4_progessbar");
var form_5_progessbar = document.querySelector(".form_5_progessbar");


var btn_done = document.querySelector(".btn_done");
var modal_wrapper = document.querySelector(".modal_wrapper");
var shadow = document.querySelector(".shadow");
var efect_confetti= document.querySelector("#my-canvas")
var close_modal=document.querySelector(".close_modal");

var _objetivo;
var _estimado_ventas;
var _presupuesto_inversion;
var _ads;
var _cantidad_trabajadores;
var _agencia;
var _identidad_marca;
var _suma=0;

form_1_next_btn.addEventListener("click", function(){
	form_1.style.display = "none";
	form_2.style.display = "block";

	form_1_btns.style.display = "none";
	form_2_btns.style.display = "flex";

	form_2_progessbar.classList.add("active");
});

form_2_back_btn.addEventListener("click", function(){
	form_1.style.display = "block";
	form_2.style.display = "none";

	form_1_btns.style.display = "flex";
	form_2_btns.style.display = "none";

	form_2_progessbar.classList.remove("active");
});

form_2_next_btn.addEventListener("click", function(){
	form_2.style.display = "none";
	form_3.style.display = "block";

    form_2_btns.style.display = "none";
	form_3_btns.style.display = "flex";

	form_3_progessbar.classList.add("active");
});

form_3_back_btn.addEventListener("click", function(){
	form_2.style.display = "block";
	form_3.style.display = "none";

    form_2_btns.style.display = "flex";
	form_3_btns.style.display = "none";

	form_3_progessbar.classList.remove("active");
});

form_3_next_btn.addEventListener("click", function(){
	form_3.style.display = "none";
	form_4.style.display = "block";

    form_3_btns.style.display = "none";
	form_4_btns.style.display = "flex";

	form_4_progessbar.classList.add("active");
});

form_4_back_btn.addEventListener("click", function(){
	form_3.style.display = "block";
	form_4.style.display = "none";

    form_3_btns.style.display = "flex";
	form_4_btns.style.display = "none";

	form_4_progessbar.classList.remove("active");
});

form_4_next_btn.addEventListener("click", function(){
    
    // var radio_publicidadads = document.getElementsByName('flexRadioPublicidadAds');
    // for (var radio of radio_publicidadads)
    // {
    //     if (radio.checked) {
    //         _ads= radio.value;
    //     }
    // }
    
    form_4.style.display = "none";
	form_5.style.display = "block";

	form_4_btns.style.display = "none";
    form_5_btns.style.display = "flex";

	form_5_progessbar.classList.add("active");
});


form_5_back_btn.addEventListener("click", function(){
	form_4.style.display = "block";
	form_5.style.display = "none";

    form_4_btns.style.display = "flex";
	form_5_btns.style.display = "none";

	form_5_progessbar.classList.remove("active");
});


btn_save.addEventListener("click", function(){
	// modal_wrapper.classList.add("active");
    // efect_confetti.classList.add("active");
	alert('Conforme')
})

shadow.addEventListener("click", function(){
	modal_wrapper.classList.remove("active");
    efect_confetti.classList.remove("active");
})

close_modal.addEventListener("click", function(){
	modal_wrapper.classList.remove("active");
    efect_confetti.classList.remove("active");
})


