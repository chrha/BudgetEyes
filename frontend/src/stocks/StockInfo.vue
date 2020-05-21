<template>
    <div id='stock-info'>
     <h3 v-for="inf in info" :key="inf.text" >{{inf.text}}</h3> <br/>
     <li v-for="feature in features" :key="feature.text">
        {{feature.text}} 
     </li>
    </div>
</template>

<script>
export default {
  name: 'StockInfo',
  data() {
    return {
      title: 'Interested in Stocks?',
      info: [
        { text: 'It is highly pleasant and efficient to be able to have an overview of' },
        { text: 'stocks that you may be interested in, in a single place.' },
        { text: 'This page provides such functionality where you can:' },
      ],
      features: [
        { text: 'Search for particular stocks' },
        { text: 'Browse some of the more popular ones' },
        { text: 'Log stocks you are interested in.' },
      ],
    };
  },
};
</script>
