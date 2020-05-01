<template>
    <div id="stock-log">
        <b-container>
            <b-row class="mb-5">
                <b-col>
                    <b-button class= "stockPageButton"> Follow</b-button> 
                </b-col>

                <b-col >
                    <b-button class= "stockPageButton">Buy</b-button>
                </b-col>
            </b-row>

            <b-row>
           
            <b-col >
            
                <b-dropdown text="Followed Stocks" >
                    <b-dropdown-item active>Placeholder1
                    </b-dropdown-item>
                    <b-dropdown-divider></b-dropdown-divider>   
                    <b-dropdown-item active>Placeholder2</b-dropdown-item>
                    <b-dropdown-divider></b-dropdown-divider>                  
                  </b-dropdown>             
            </b-col>

            <b-col >
                <b-dropdown text="Bought Stocks" >
                    <b-dropdown-item active>Placeholder2</b-dropdown-item>
                    <b-dropdown-divider></b-dropdown-divider>   
                    <b-dropdown-item active>Placeholder3</b-dropdown-item>
                    <b-dropdown-divider></b-dropdown-divider>                  
                  </b-dropdown>   
                      
            </b-col>
            </b-row>
        </b-container>
    </div>
</template>


<script>
export default {
  name: 'StockLog',
};
</script>



<style>
    .stockPageButton{
        background-color: #C7F0DB;
        color: #000000;
        
    }
</style>
