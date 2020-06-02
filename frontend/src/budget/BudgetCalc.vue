
<template>
  <div class="block">
    <div class="center">
      <h4 class="text-left"> {{ intro }} </h4>

      <v-text-field
        label ="Income"
        v-model=income
        @change="income = $event">
      </v-text-field>

      <div>
        <v-text-field
        v-for="expense in firstExpense"
        v-bind:key="expense.id"
        v-bind:label="$value(expense.name)"
        v-model="expense.value"
        @change="expense.value = $event">

        <template slot="append">
           <v-btn outlined style="margin-bottom: 6px"
           v-on:click="$changeType(expense)">
                   {{expense.type}}
           </v-btn>
        </template>

        <v-icon
        slot="append"
        v-on:click="incramentCounter"
        >mdi-plus</v-icon>

        </v-text-field>
      </div>

        <div>
          <v-text-field
          v-for="expense in restExpenses"
          v-bind:key="expense.id"
          v-bind:label="$value(expense.name)"
          v-model="expense.value"
          @change="expense.value = $event">

            <template slot="append">
               <v-btn outlined style="margin-bottom: 6px"
               v-on:click="$changeType(expense)">
                       {{expense.type}}
               </v-btn>
            </template>

            <v-icon
            slot="append"
            v-on:click="$remove(expense)">mdi-minus</v-icon>

          </v-text-field>
        </div>

      <v-btn small v-if="showFetch" v-on:click="fetchData">
        Load your saved income and expenses</v-btn>
      <v-btn small v-if="showSave" v-on:click="saveData">Save your income and expenses</v-btn>

      <br> <br>
      <v-btn small v-on:click="calculateBudget">Calculate Budget</v-btn>
      <v-divider light ></v-divider>
      <div
      v-if="showResult">
        <div class="result">

        <h2 class="head">Need</h2>
        <v-progress-linear
          color="deep-orange"
          height="20"
          rounded=true
          v-model="budget[0].procentage"
          striped
        >
          <template v-slot="{ value }">
            <strong>{{ Math.ceil(value) }}%</strong>
          </template>
        </v-progress-linear>
        <p>
          Used: {{budget[0].used}} <br>
          Limit: {{budget[0].limit}} <br>
        </p>
        <h2 class="head">Want</h2>
        <v-progress-linear
          color="blue"
          height="20"
          rounded=true
          v-model="budget[1].procentage"
          striped
        >
          <template v-slot="{ value }">
            <strong>{{ Math.ceil(value) }}%</strong>
          </template>
        </v-progress-linear>
        <p>
          Used: {{budget[1].used}} <br>
          Limit: {{budget[1].limit}} <br>
        </p>
        <h2 class="head">Savings</h2>
        <v-progress-linear
          color="deep-purple accent-4"
          height="20"
          rounded=true
          v-model="budget[2].procentage"
          striped
        >
        <template v-slot="{ value }">
          <strong>{{ Math.ceil(value) }}%</strong>
        </template>
        </v-progress-linear>
        <p>
          Used: {{budget[2].used}} <br>
          Limit: {{budget[2].limit}} <br>
        </p>
        <br>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from '../ajax/client';

export default {
  name: 'BudgetCalc',
  data() {
    return {
      expenses: [
        {
          name: 'Expense',
          value: '',
          first: 'true',
          type: 'Need',
        },
      ],
      count: 1,
      intro: 'Enter monthly income and expenses to find out your budget!',
      income: '',
      budget: [
        {
          type: 'Need',
          limit: 0,
          used: 0,
          procentage: 0,
        },
        {
          type: 'Want',
          limit: 0,
          used: 0,
          procentage: 0,
        },
        {
          type: 'Saving',
          total: 0,
          used: 0,
          procentage: 0,
        },
      ],
      showResult: false,
      showFetch: false,
      showSave: false,
    };
  },
  created() {
    axiosInstance.get('budget/income/', { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
      .then((response) => {
        if (response.data.income === null) {
          this.showFetch = false;
          this.showSave = true;
        } else {
          this.showFetch = true;
          this.showSave = false;
        }
      }).catch((error) => {
        this.showFetch = false;
        this.showSave = false;
        // eslint-disable-next-line
        console.log(error);
      });
    axiosInstance.get('budget/expenses/', { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
      .then((response) => {
        if (response.data) {
          this.showFetch = this.showFetch || false;
          this.showSave = this.showSave && true;
        } else {
          this.showFetch = true;
          this.showSave = false;
        }
      }).catch((error) => {
        this.showFetch = false;
        this.showSave = false;
        // eslint-disable-next-line
        console.log(error);
      });
  },
  computed: {
    firstExpense() {
      return this.expenses.filter((i) => i.first === 'true');
    },
    restExpenses() {
      return this.expenses.filter((i) => i.first === 'false');
    },
  },
  methods: {
    saveData() {
      let data = {
        income: this.income,
      };
      axiosInstance.put('budget/income/', data, { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then(() => {
        }).catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });

      data = {
        expenses: this.expenses,
      };
      axiosInstance.put('budget/expenses/', data, { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then(() => {
        }).catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });
    },
    fetchData() {
      axiosInstance.get('budget/income/', { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then((response) => {
          this.income = response.data.income;
          this.showFetch = false;
          this.showSave = true;
        }).catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });
      axiosInstance.get('budget/expenses/', { headers: { Authorization: `Token ${this.$cookies.get('token')}` } })
        .then((response) => {
          this.count = 1;
          this.expenses = [
            {
              name: 'Expense',
              value: response.data[0].sum,
              first: 'true',
              type: response.data[0].type,
            },
          ];
          for (let i = 1; i < response.data.length; i += 1) {
            this.count += 1;
            this.expenses.push({
              name: 'Expense',
              value: response.data[i].sum,
              first: 'false',
              type: response.data[i].type,
            });
            this.showFetch = false;
            this.showSave = true;
          }
        }).catch((error) => {
        // eslint-disable-next-line
        console.log(error);
        });
    },
    incramentCounter() {
      this.count += 1;
      this.expenses.push({
        name: 'Expense',
        value: '',
        first: 'false',
        type: 'Need',
      });
    },
    $value(value) {
      return value;
    },
    calculateBudget() {
      let usedNeed = 0;
      let usedWant = 0;
      let usedSavings = 0;
      let i;
      this.showResult = true;
      for (i = 0; i < this.count; i += 1) {
        if (this.expenses[i].type === 'Need') {
          usedNeed += parseInt(this.expenses[i].value, 10);
        } else if (this.expenses[i].type === 'Want') {
          usedWant += parseInt(this.expenses[i].value, 10);
        } else {
          usedSavings += parseInt(this.expenses[i].value, 10);
        }
      }
      this.budget[0].used = usedNeed;
      this.budget[1].used = usedWant;
      this.budget[2].used = usedSavings;
      const total = parseInt(this.income, 10);

      this.budget[0].limit = Math.floor(0.5 * total);
      this.budget[1].limit = Math.floor(0.3 * total);
      this.budget[2].limit = Math.floor(0.2 * total);

      this.budget[0].procentage = 100 * (usedNeed / Math.floor(0.5 * total));
      this.budget[1].procentage = Math.floor(100 * (usedWant / Math.floor(0.3 * total)));
      this.budget[2].procentage = Math.floor(100 * (usedSavings / Math.floor(0.2 * total)));
    },
    $remove(expense) {
      const i = this.expenses.indexOf(expense);
      this.count -= 1;
      this.expenses.splice(i, 1);
    },
    $changeType(expense) {
      const i = this.expenses.indexOf(expense);
      if (this.expenses[i].type === 'Need') {
        this.expenses[i].type = 'Want';
      } else if (this.expenses[i].type === 'Want') {
        this.expenses[i].type = 'Savings';
      } else {
        this.expenses[i].type = 'Need';
      }
    },
  },
};

</script>

<style scoped>
.text-left{
  margin-top:30px;
}
.head{
  text-align: left;
}
</style>
