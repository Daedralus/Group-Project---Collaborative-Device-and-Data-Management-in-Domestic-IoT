using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Core;
using MongoDB.Bson.IO;
using Newtonsoft.Json;
using System.Threading.Tasks;

using System.Drawing;
using System.Web.Http;
using System.IO;

namespace Services.Actions
{
    public class Application
    {
        public static List<object> ListResidents()
        {
            var collection = DB.Database.GetCollection<BsonDocument>("Residents");
            var projection = Builders<BsonDocument>.Projection.Exclude("_id");
            var filter = Builders<BsonDocument>.Filter.Empty;

            var document = collection.Find(filter).Project(projection).ToEnumerable().OrderBy(x => x["NAME"]).ToList();
            var jsonWriterSettings = new JsonWriterSettings { OutputMode = JsonOutputMode.Strict }; // key part
            var doc = document.ToJson(jsonWriterSettings);
            var result = Newtonsoft.Json.JsonConvert.DeserializeObject<List<object>>(doc);
            return result;
        }
    }
}