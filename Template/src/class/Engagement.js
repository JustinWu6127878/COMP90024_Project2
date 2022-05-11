class Engagement {
    constructor (male, edu, income, overper){
        this.male = male;
        this.female = 100-male;
        this.edu = edu;
        this.income = income;
        this.overper = overper;
    }
}

export default Engagement