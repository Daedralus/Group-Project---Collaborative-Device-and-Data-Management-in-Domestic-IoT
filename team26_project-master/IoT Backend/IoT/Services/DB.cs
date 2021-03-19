using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Services
{
    public static class DB
    {
        private static MongoClient m_client;
        private static IMongoDatabase m_database;
        public static MongoClient Client { get => m_client; }
        public static IMongoDatabase Database { get => m_database; }

        static DB()
        {
        }

        public static void Init()
        {
            //m_client = new MongoClient("mongodb://192.168.1.180:27017");
            m_client = new MongoClient("mongodb://localhost:27017");
            m_database = m_client.GetDatabase("IoT");
        }
    }
}