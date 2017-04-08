<template>
  <div>
    <nav class="navbar navbar-default navbar-static-top">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">
                    BGG Game Filtering
                </a>
            </div>
        </div>
    </nav>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </div>
</template>

<script>
// Start the View instance on the Application
export default {
  name: 'app'
}
</script>

<style>
body {
  background-color: #EEE;
}

</style>
