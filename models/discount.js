var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var DiscountSchema = new Schema({
  name:{type:String, required:true},
  value:{type:Number, required: true}
});

module.export = mongoose.model('Discount', DiscountSchema);
