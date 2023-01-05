using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO.Ports;


public class RotateOneFinger : MonoBehaviour
{
    public Transform J1, P1;
    public Transform J2_1, P2_1, J2_2, P2_2;
    public Transform J3_1, P3_1, J3_2, P3_2;
    public Transform J4_1, P4_1, J4_2, P4_2;
    public Transform J5, P5;

    SerialPort data_stream = new SerialPort("\\\\.\\COM14", 9600);
    public string receivedstring;
    public int recv_angle_J1;

    public int recv_angle_J2_1;
    public int recv_angle_J2_2;

    public int recv_angle_J3_1;
    public int recv_angle_J3_2;

    public int recv_angle_J4_1;
    public int recv_angle_J4_2;

    public int recv_angle_J5;


    // Start is called before the first frame update
    void Start()
    {
        data_stream.Open();
    }

    // Update is called once per frame
    void Update()
    {

        receivedstring = data_stream.ReadLine();
        int str_to_int = Mathf.RoundToInt(int.Parse(receivedstring));

        if (str_to_int==1100)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J1 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else if (str_to_int == 2100)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J2_1 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else if (str_to_int == 2200)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J2_2 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else if (str_to_int == 3100)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J3_1 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else if (str_to_int == 3200)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J3_2 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else if (str_to_int == 4100)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J4_1 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else if (str_to_int==4200)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J4_2 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else if (str_to_int == 5100)
        {
            receivedstring = data_stream.ReadLine();
            recv_angle_J5 = Mathf.RoundToInt(int.Parse(receivedstring));
        }
        else
        {
            recv_angle_J1 = 0;

            recv_angle_J2_1 = 0;
            recv_angle_J2_2 = 0;

            recv_angle_J3_1 = 0;
            recv_angle_J3_2 = 0;

            recv_angle_J4_1 = 0;
            recv_angle_J4_2 = 0;

            recv_angle_J5 = 0;
        }

        J1.transform.eulerAngles = new Vector3(-recv_angle_J1, -90, 90);

        J2_1.transform.eulerAngles = new Vector3(0, -recv_angle_J2_1, 0);
        J2_2.transform.eulerAngles = new Vector3(0, -(recv_angle_J2_1 + recv_angle_J2_2), 0);

        J3_1.transform.eulerAngles = new Vector3(0, -recv_angle_J3_1, 0);
        J3_2.transform.eulerAngles = new Vector3(0, -(recv_angle_J3_1 + recv_angle_J3_2), 0);

        J4_1.transform.eulerAngles = new Vector3(0, -recv_angle_J4_1, 0);
        J4_2.transform.eulerAngles = new Vector3(0, -(recv_angle_J4_1 + recv_angle_J4_2), 0);

        J5.transform.eulerAngles = new Vector3(0, -recv_angle_J5, 0);
    }
}