# ML
Option Explicit

Sub d()
    Dim d&
    With Sheets("Íåäîñòà÷à")
        For d = 2 To .Cells(Rows.Count, 1).End(xlUp).Row
            If .Cells(d, 3).Value <> "" Then
                .Rows(d).EntireRow.Delete
            End If
        Next
    End With
End Sub

Sub del_zero()
    Dim arr1()
    Dim arr2()
    Dim j As Long
    Dim li As Long
    Dim i As Long
    Dim ii As Long
    Dim iColumns As Integer
On Error GoTo err:
    For li = 2 To Sheets(1).Cells(Rows.Count, 3).End(xlUp).Row
        If Sheets(1).Range("C" & li).Value = "" Then
            With Sheets(1).Range("A2").CurrentRegion
                iColumns = .Columns.Count
                ReDim arr2(1 To .Rows.Count, 1 To iColumns)
                arr1 = .Value
                For j = 1 To .Rows.Count
                    If arr1(j, 3) <> "" Then
                        i = i + 1
                        For ii = 1 To iColumns
                            arr2(i, ii) = arr1(j, ii)
                        Next
                    End If
                Next
                Sheets(1).Range("A1:C" & Cells(Rows.Count, 1).End(xlUp).Row).ClearContents
                Sheets(1).Range("A1").Resize(i, iColumns).Value = arr2
            End With
        End If
    Next
Exit Sub
err:
End Sub

Sub del_full()
    Dim arr1()
    Dim arr2()
    Dim j As Long
    Dim li As Long
    Dim i As Long
    Dim ii As Long
    Dim iColumns As Integer
On Error GoTo err:
    For li = 2 To Sheets(1).Cells(Rows.Count, 3).End(xlUp).Row
        If Sheets(1).Range("C" & li).Value <> "" Then
            With Sheets(1).Range("A1").CurrentRegion
                iColumns = .Columns.Count
                ReDim arr2(1 To .Rows.Count, 1 To iColumns)
                arr1 = .Value
                For j = 1 To .Rows.Count
                    If arr1(j, 3) = "" Then
                        i = i + 1
                        For ii = 1 To iColumns
                            arr2(i, ii) = arr1(j, ii)
                        Next
                    End If
                Next
                Sheets(1).Range("A1:C" & Cells(Rows.Count, 1).End(xlUp).Row).ClearContents
                Sheets(1).Range("A1").Resize(i, iColumns).Value = arr2
            End With
        End If
    Next
Exit Sub
err:
End Sub
