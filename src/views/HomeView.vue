<template>
  
  <body>
    <TheHeader></TheHeader>
    <div class="max-w-max mx-auto">

      <div class="text-center text-white w-[900px] mt-[100px] lg:w-[650px]">
        <div class="title-text">
          <h1 class="text-[68px] leading-[70px]">Looking like the best bot for polls and suggestions</h1>
          <br>
          <p class="text-light-purple text-[28px] mx-10">Mr Poll is a question and feedback Discord bot powering <b>35k+</b> servers.</p>
          <div class="m-[28px]">
            <a class="main-btn" href="/invite">Add Mr Poll</a>
            <a class="main-btn" href="#">Dashboard</a>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULES -->
    <div class="max-w-max mx-auto">
      <div class="text-white w-[900px] mt-[250px] lg:w-[650px]">

        <section>
          <h2>Bot Modules</h2>
          <p class="hint">Click on a module to learn more!</p>
  
          <div class="flex justify-between mt-[50px] lg:block">
  
            <div class="module-btn" @click="goToModule('poll')">
              <img src="../assets/placeholder.png">
              <h3>Polls</h3>
              
            </div>
            <div class="module-btn" @click="goToModule('quizzes')">
              <img src="../assets/placeholder.png">
              <h3>Quizzes</h3>
            </div>
            <div class="module-btn" @click="goToModule('suggestions')">
              <img src="../assets/placeholder.png">
              <h3>Suggestions</h3>
            </div>
  
          </div>
        </section>

        
      </div>
    </div>

    <!-- REVIEWS -->
    <div class="max-w-max mx-auto">
      <div class="text-white w-[900px] mt-[160px] lg:w-[650px]">

        <section>
          <h2>Reviews</h2>
          <p class="hint">What do people think about Mr Poll?</p>
  
          <div class="justify-between mt-[50px] reviews">
  
            <div class="review">
              <img src="https://u.viadev.xyz/avatar/750310441800040478" alt="a very conos guy">
              <div class="text">
                <p class="username">Conos <span>— Owner of NFT giveaways (10k+ members)</span></p>
                <p class="comment">... blocked.</p>
              </div>
            </div>
            <div class="review">
              <img src="https://u.viadev.xyz/avatar/402888568579686401" alt="a very conos guy">
              <div class="text">
                <p class="username">Conos <span>— Owner of NFT giveaways (10k+ members)</span></p>
                <p class="comment">“Mr Poll made my family love me again! Without it, i would have no idea what they want from me!”</p>
              </div>
            </div>
            <div class="review">
              <img src="https://u.viadev.xyz/avatar/750310441800040478" alt="a very conos guy">
              <div class="text">
                <p class="username">Conos <span>— Owner of NFT giveaways (10k+ members)</span></p>
                <p class="comment">... blocked.</p>
              </div>
            </div>
  
          </div>
        </section>

        
      </div>
    </div>

  </body>
  <TheFooter></TheFooter>
</template>

<script>
// @ is an alias to /src
import  TheHeader  from "../components/Header.vue";
import  TheFooter  from "../components/Footer.vue";
export default {
  name: 'HomeView',

  components: {
    TheHeader, TheFooter
  },
  methods: {
    goToModule (route) {
      window.location.href = `/module/${route}`
    },
  }
}
</script>


<style scoped>



/* SECTION */
/* 
section {
  @apply max-w-max mx-auto text-white w-[900px] mt-[250px]
} */

h2 {
  @apply text-white text-[40px]
}

.hint {
  @apply text-light-purple text-[22px]
}

/* BUTTONS */

.main-btn {
  @apply bg-purple p-4 rounded-md m-2 text-2xl hover:bg-button-hover duration-300 ease-out
}


.module-btn {
  @apply bg-purple p-2 w-[290px] rounded-lg text-[25px] cursor-pointer h-[190px] hover:bg-button-hover duration-300 ease-out lg:mt-16 lg:w-full
}

.module-btn img {
  @apply relative bottom-6 left-4 w-[300px] lg:left-72 lg:bottom-0
}

.module-btn h3 {
  @apply relative bottom-5 left-4 lg:bottom-12 lg:text-4xl lg:rotate-12 lg:left-8
}

/* REVIEWS SECTION */

.review {
  @apply block w-full mb-[100px] px-2 rounded-[5px];
  /* From https://css.glass */
  background: rgba(114, 44, 224, 0.5);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
}

.reviews:last-child {
  @apply mb-0
}


.review img { 
  @apply inline-block w-[100px] relative bottom-6 rounded-[9px] bg-[#000] ml-4 align-top
}

.review .text {
  @apply inline-block w-[650px] ml-4 p-4
}

.review .username {
  @apply text-[25px]
}

.review .username span {
  @apply text-[22px] font-normal font-[Gothamb]
}

.review .comment {
  @apply text-[#D5D5D5] text-[22px] font-normal font-[Gothamb]
}


</style>