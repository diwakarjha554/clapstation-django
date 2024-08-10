let icon = document.querySelector(".menu-icon");
let ull = document.querySelector(".nav-bar");
let ulll = document.querySelector("ul");

icon?.addEventListener("click", ()=>{
    ull.classList.toggle("showdata");
    ulll.classList.toggle("column")
    console.log(ull);
})



// Home Upload Post Modal 

const homePostUploadTrigger = document.querySelector('#homePostUploadTrigger');
const homeUploadModalWrapper = document.querySelector('.home-upload-post-modal-wrapper');
const homeUploadCloseButton = document.querySelector('#homeUploadCloseButton');
const homePostUploadBtn = document.querySelector('#homePostUploadBtn');


homePostUploadTrigger?.addEventListener('click', function(){
    homeUploadModalWrapper.classList.add('opacityTrigger');
});

homePostUploadBtn?.addEventListener('click', function(){
    homeUploadModalWrapper.classList.add('opacityTrigger');
});

homeUploadCloseButton?.addEventListener('click', function(){
    homeUploadModalWrapper.classList.remove('opacityTrigger');
});

homeUploadModalWrapper?.addEventListener('click', function(e){
    if(e.target !== this) return;

    homeUploadModalWrapper.classList.remove('opacityTrigger');
});

document?.addEventListener('keydown', function(e){
    if(e.key == 'Escape'){
        homeUploadModalWrapper.classList.remove('opacityTrigger');
    }
});


// 

const imgInput = document.querySelector("#img-input")
const displayImg = document.querySelector("#display-img")
imgInput?.addEventListener('change',(event)=>{
   const imgObject = event.target.files[0]
   displayImg.src = URL.createObjectURL(imgObject)
});



// Home Events Post Modal 

const homeEventsUploadTrigger = document.querySelector('#homeEventsBtn');
const homeEventsModalWrapper = document.querySelector('.home-events-icon-modal-wrapper');
const homeEventsCloseButton = document.querySelector('#homeEventsCloseButton');


homeEventsUploadTrigger?.addEventListener('click', function(){
    homeEventsModalWrapper.classList.add('opacityTrigger');
});


homeEventsCloseButton?.addEventListener('click', function(){
    homeEventsModalWrapper.classList.remove('opacityTrigger');
});

homeEventsModalWrapper?.addEventListener('click', function(e){
    if(e.target !== this) return;

    homeEventsModalWrapper.classList.remove('opacityTrigger');
});

document?.addEventListener('keydown', function(e){
    if(e.key == 'Escape'){
        homeEventsModalWrapper.classList.remove('opacityTrigger');
    }
});





// Posts Three dots (ellipsis) modal

const threeDotsMenus = document.querySelectorAll('.three-dots-menu');
const postView = document.querySelectorAll('.post-view-more-option');

postView.forEach((postViewElement) => {
    const threeDotsIdTrigger = postViewElement.querySelector('.three-dots-class');

    threeDotsIdTrigger?.addEventListener('click', function(){
        const threeDotsMenu = this.nextElementSibling; 
        threeDotsMenu.classList.toggle('opacityTrigger');
    });
});


// Comment Modal
const cmmntTrigger = document.querySelector('#cmmntTrigger');
const cmmntWrapper = document.querySelector('.post-cmmnt-btn-modal-wrapper');
const cmmntCloseButton = document.querySelector('#cmmntCloseButton');
const cmmntSubmitBtn = document.querySelector('#cmmntSubmitBtn');


cmmntTrigger?.addEventListener('click', function(){
    cmmntWrapper.classList.add('opacityTrigger');
});

cmmntCloseButton?.addEventListener('click', function(){
    cmmntWrapper.classList.remove('opacityTrigger');
});

cmmntWrapper?.addEventListener('click', function(e){
    if(e.target !== this) return;

    cmmntWrapper.classList.remove('opacityTrigger');
});

document?.addEventListener('keydown', function(e){
    if(e.key == 'Escape'){
        cmmntWrapper.classList.remove('opacityTrigger');
    }
});



// Edit Profile modal

const editProfileTrigger = document.querySelector('#editProfileTrigger');
const editProfileWrapper = document.querySelector('.edit_profile_wrapper');
const editProfileClosseBtn = document.querySelector('.edit_profile_close');

editProfileTrigger?.addEventListener('click', function(){
    editProfileWrapper.classList.add('opacityTrigger');
});

editProfileClosseBtn?.addEventListener('click', function(){
    editProfileWrapper.classList.remove('opacityTrigger');
});

editProfileWrapper?.addEventListener('click', function(e){
    if(e.target !== this) return;

    editProfileWrapper.classList.remove('opacityTrigger');
});

document?.addEventListener('keydown', function(e){
    if(e.key == 'Escape'){
        editProfileWrapper.classList.remove('opacityTrigger');
    }
});