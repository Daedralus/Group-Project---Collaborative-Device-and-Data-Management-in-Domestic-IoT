using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Http;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;

using Services.Actions;

namespace Services.Controllers
{
    public class DefaultController : ApiController
    {
        [HttpGet]
        public List<object> ListResidents()
        {
            return Application.ListResidents();
        }

        public void Post(string v)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<string> Get()
        {
            throw new NotImplementedException();
        }

        public string Get(int v)
        {
            throw new NotImplementedException();
        }
    }
}
