
<template>
<div id="navbar-app">
    <div>
        <b-navbar class = "navbar">
            <b-navbar-brand href="#">
                <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/f/f0/Eye-Brown.svg" alt="BE" style="width:40px;height:40px;">
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse class="nav-collapse" is-nav>
                <b-navbar-nav class="navbar-nav">
                    <b-nav-item class="navbar-item-custom" href="#">Budget</b-nav-item>
                    <b-nav-item class="navbar-item-custom" href="#">Stocks</b-nav-item>
                </b-navbar-nav>

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <b-nav-form>
                        <b-form-input size="sm" class="mr-sm-3" placeholder="Search"></b-form-input>
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                    </b-nav-form>

                    <b-nav-item-dropdown right>
                        <!-- Using 'button-content' slot -->
                        <template v-slot:button-content>
                            <em> {{ user.get_username }}</em>
                        </template>
                        <b-dropdown-item href="#">Profile</b-dropdown-item>
                        <b-dropdown-item href="/logout/">Sign Out</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</div>
</template>



<script>
export default {
  name: 'navBar',
};
</script>


 <style>
    .navbar .nav-collapse .navbar-nav .navbar-item-custom{
        color: #b30b0b;
    }
    .navbar{
    background-color: #6c7b95;
    height: 40px;
    }
    .logo{
        size: 20px;
    }

</style>
