<template>
  <header class="text-white p-8 grid grid-cols-3 items-center">
    <div class="flex items-center justify-start">
      <div class="logo">
        <img class="w-7 h-auto mr-[10px]" src="../assets/pollwwhite.png">
      </div>
      <div class="text-3xl text-white">Mr Poll</div>
    </div>

    <nav class="flex justify-center">
      <ul class="flex gap-4 text-2xl">
        <li><a href="#" class="nav-link">Modules</a></li>
        <li><a href="#" class="nav-link">Dashboard</a></li>
      </ul>
    </nav>
    <div class="flex justify-end"></div> <!-- Empty placeholder for balancing -->
  </header>
</template>
  
<script>
export default {
  name: 'TheHeader',
}
</script>
  

<style scoped>
.nav-link {
  @apply text-white inline-block relative mx-4
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #FFF;
  transform-origin: bottom right;
  transition: transform 0.3s ease-out;
}

.nav-link:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}
</style>
  