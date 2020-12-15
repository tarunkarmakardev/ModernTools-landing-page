// let NavItem = document.querySelectorAll('.nav-cus-menu .navbar-nav .nav-link');
// // console.log(NavItem);

// NavItem.forEach(item => {
//     item.addEventListener('click', () => {

//         NavItem.forEach(item => {
//             item.classList.remove('active');
//         });
//         item.classList.add('active');


//     });
// });

// Animation using Intersection observer for all '.fade-in .row' 

let animateElements = document.querySelectorAll(".fade-in .row");
// console.log(animateElements);

let observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.intersectionRatio > 0) {
            entry.target.style.animation = `fadeIn 1.5s ease`;
        }
        else {
            entry.target.style.animation = 'none';
        }

    })
});

animateElements.forEach((element) => {
    observer.observe(element);
})

// Animation using Intersection observer for navbar:

let nav = document.querySelector('nav');
let navBrandText = document.querySelector('.navbar-brand span');
let firstSection = document.querySelector('.first-section');

let firstSectionOptions = {
    rootMargin: "-100px 0px 0px 0px"
};

// console.log(firstSection);
// console.log(nav);
// console.log(navBrandText);

let navObeserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (!entry.isIntersecting) {
            nav.classList.remove("bg-alpha");
            nav.classList.add("bg-beta-light", "nav-text-change");
            navBrandText.classList.add("nav-text-change");
        }
        else {
            nav.classList.add("bg-alpha");
            nav.classList.remove("bg-beta-light", "nav-text-change");
            navBrandText.classList.remove("nav-text-change");
        }
    })
}, firstSectionOptions);

navObeserver.observe(firstSection);


// Making social links to open in new tab:

let newTabLinks = document.querySelectorAll(".new-tab a");
// console.log(newTabLinks);

newTabLinks.forEach(link => { link.setAttribute("target", "_blank") });

// all console.log(); are for debugging!